"""empty message

Revision ID: fda0c63d9572
Revises: 4c230f669068
Create Date: 2024-11-28 17:24:48.152979

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fda0c63d9572'
down_revision: Union[str, None] = '4c230f669068'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('category')
    op.alter_column('cities', 'latitude',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('cities', 'longitude',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.add_column('completed_routes', sa.Column('route_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'completed_routes', 'routes', ['route_id'], ['id'])
    op.add_column('places', sa.Column('route_id', sa.Integer(), nullable=False))
    op.add_column('places', sa.Column('category_id', sa.Integer(), nullable=False))
    op.alter_column('places', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('places', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('places', 'latitude',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('places', 'longitude',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('places', 'opening_hours',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_foreign_key(None, 'places', 'routes', ['route_id'], ['id'])
    op.create_foreign_key(None, 'places', 'categories', ['category_id'], ['id'])
    op.add_column('routes', sa.Column('city_id', sa.Integer(), nullable=False))
    op.alter_column('routes', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('routes', 'duration',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('routes', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('routes', 'distance',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('routes', 'updated_at',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_foreign_key(None, 'routes', 'cities', ['city_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'routes', type_='foreignkey')
    op.alter_column('routes', 'updated_at',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('routes', 'distance',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('routes', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('routes', 'duration',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('routes', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('routes', 'city_id')
    op.drop_constraint(None, 'places', type_='foreignkey')
    op.drop_constraint(None, 'places', type_='foreignkey')
    op.alter_column('places', 'opening_hours',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('places', 'longitude',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('places', 'latitude',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('places', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('places', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('places', 'category_id')
    op.drop_column('places', 'route_id')
    op.drop_constraint(None, 'completed_routes', type_='foreignkey')
    op.drop_column('completed_routes', 'route_id')
    op.alter_column('cities', 'longitude',
               existing_type=sa.String(length=100),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.alter_column('cities', 'latitude',
               existing_type=sa.String(length=100),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.create_table('category',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='category_pkey')
    )
    op.drop_table('categories')
    # ### end Alembic commands ###
