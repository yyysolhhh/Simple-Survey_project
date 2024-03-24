import json

import pandas as pd
import plotly  # type: ignore
import plotly.express as px  # type: ignore
from plotly.graph_objs import Figure  # type: ignore

from app.models.answer import Answer
from app.models.participant import Participant
from app.models.question import Question


async def extract_to_dataframe() -> pd.DataFrame:
    participants_list = await Participant.get_all_participants()
    # self.answers_list = await Answer.get_all_answers()
    participants_data = [{"age": participant.age, "gender": participant.gender} for participant in participants_list]
    # answers_data = [
    #     {
    #         "question_id": answer.question,
    #         "choice": answer.choice,
    #         "participant_age": Participant.get_one_by_id(answer.participant_id).age,
    #     }
    #     for answer in answers_list
    # ]
    participants_df = pd.DataFrame(participants_data)
    return participants_df


def create_graph_age_distribution(participants_df: pd.DataFrame) -> Figure:
    return px.pie(
        participants_df,
        names="age",
        title="Age Distribution",
        hole=0.3,
        labels={"age": "Age"},
        color_discrete_sequence=px.colors.sequential.RdBu,
    )


def create_graph_gender_distribution(participants_df: pd.DataFrame) -> Figure:
    return px.pie(
        participants_df,
        names="gender",
        title="Gender Distribution",
        hole=0.3,
        labels={"gender": "Gender"},
        color_discrete_sequence=px.colors.sequential.RdBu,
    )


async def get_result_graphs() -> str:
    participants_df = await extract_to_dataframe()
    print(participants_df)
    fig_age = create_graph_age_distribution(participants_df)
    fig_gender = create_graph_gender_distribution(participants_df)
    graphs_json = json.dumps(
        {
            "age_distribution": fig_age,
            "gender_distribution": fig_gender,
        },
        cls=plotly.utils.PlotlyJSONEncoder,
    )
    return graphs_json
