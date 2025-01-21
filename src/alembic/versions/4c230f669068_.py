"""empty message

Revision ID: 4c230f669068
Revises: eb464694915a
Create Date: 2024-11-28 16:58:42.664251

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c230f669068'
down_revision: Union[str, None] = 'eb464694915a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cities', sa.Column('latitude', sa.Integer(), nullable=True))
    op.add_column('cities', sa.Column('longitude', sa.Integer(), nullable=True))
    op.drop_column('cities', 'region')
    op.drop_column('cities', 'population')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cities', sa.Column('population', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('cities', sa.Column('region', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.drop_column('cities', 'longitude')
    op.drop_column('cities', 'latitude')
    # ### end Alembic commands ###
