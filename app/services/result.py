import json

import pandas as pd
import plotly  # type: ignore
import plotly.express as px  # type: ignore
from plotly.graph_objs import Figure  # type: ignore

from app.models.answer import Answer
from app.models.participant import Participant


async def extract_participants_to_dataframe() -> pd.DataFrame:
    participants_list = await Participant.get_all_participants()
    participants_data = [{"age": participant.age, "gender": participant.gender} for participant in participants_list]
    participants_df = pd.DataFrame(participants_data)
    return participants_df


async def extract_answers_to_dataframe() -> pd.DataFrame:
    answers_list = await Answer.get_answers_join_questions()
    answers_data = [
        {
            "question_id": answer.question.id,
            "choice": answer.choice,
        }
        for answer in answers_list
    ]
    answers_df = pd.DataFrame(answers_data)
    return answers_df


def create_age_distribution_graph(participants_df: pd.DataFrame) -> Figure:
    return px.pie(
        participants_df,
        names="age",
        title="Age Distribution",
        hole=0.3,
        labels={"age": "Age"},
        # color_discrete_sequence=px.colors.qualitative.Plotly,
        color_discrete_sequence=px.colors.sequential.Turbo,
    )


def create_gender_distribution_graph(participants_df: pd.DataFrame) -> Figure:
    return px.pie(
        participants_df,
        names="gender",
        title="Gender Distribution",
        hole=0.3,
        labels={"gender": "Gender"},
        color_discrete_sequence=px.colors.qualitative.Plotly,
        # color_discrete_sequence=px.colors.sequential.Plasma_r,
    )


def create_one_answers_graph(answers_df: pd.DataFrame, number: int) -> Figure:
    fig = px.pie(
        answers_df,
        names="choice",
        title=f"Question{number}",
        hole=0.3,
        labels={"choice": "Choice"},
        color_discrete_sequence=px.colors.qualitative.Plotly,
        # color_discrete_sequence=px.colors.sequential.Plasma_r,
    )
    return fig


def create_answers_graphs(answers_df: pd.DataFrame) -> dict[str, Figure]:
    answers_graphs = {}
    for question_id in answers_df.question_id.unique():
        filtered_df = answers_df[answers_df["question_id"] == question_id]
        answers_graphs[f"questions_{question_id}"] = create_one_answers_graph(filtered_df, question_id)
    return answers_graphs


async def get_result_graphs() -> str:
    participants_df = await extract_participants_to_dataframe()
    answers_df: pd.DataFrame = await extract_answers_to_dataframe()
    fig_age = create_age_distribution_graph(participants_df)
    fig_gender = create_gender_distribution_graph(participants_df)
    fig_response = create_answers_graphs(answers_df)
    graphs_json = json.dumps(
        {
            "age_distribution": fig_age,
            "gender_distribution": fig_gender,
            "responses": fig_response,
        },
        cls=plotly.utils.PlotlyJSONEncoder,
    )
    return graphs_json
