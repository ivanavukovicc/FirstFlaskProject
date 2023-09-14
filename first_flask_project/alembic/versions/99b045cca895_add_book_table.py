"""Add Book table

Revision ID: 99b045cca895
Revises: 1208f1e43cb7
Create Date: 2023-09-14 12:04:28.110149

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99b045cca895'
down_revision: Union[str, None] = '1208f1e43cb7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'book',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('naziv', sa.String(length=255), nullable=False),
        sa.Column('autor', sa.String(length=255)),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('book')
