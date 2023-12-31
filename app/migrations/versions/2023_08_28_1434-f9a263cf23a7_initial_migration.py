"""Initial migration

Revision ID: f9a263cf23a7
Revises: 
Create Date: 2023-08-28 14:34:35.762043

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f9a263cf23a7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'hotels',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('Hotel name', sa.String(length=60), nullable=False),
        sa.Column('Hotel location', sa.String(length=500), nullable=False),
        sa.Column('Hotel services', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('Rooms quantity', sa.Integer(), nullable=False),
        sa.Column('Hotel image id', sa.SmallInteger(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hotels')
    # ### end Alembic commands ###
