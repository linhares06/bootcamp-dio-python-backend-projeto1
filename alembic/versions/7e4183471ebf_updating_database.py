"""Updating database

Revision ID: 7e4183471ebf
Revises: 67ef08b7aee9
Create Date: 2024-04-25 17:56:45.594608

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e4183471ebf'
down_revision: Union[str, None] = '67ef08b7aee9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'centros_treinamento', ['nome'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'centros_treinamento', type_='unique')
    # ### end Alembic commands ###
