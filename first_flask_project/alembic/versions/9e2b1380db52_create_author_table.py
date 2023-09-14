"""create author table

Revision ID: 9e2b1380db52
Revises: 807a35f4e8c8
Create Date: 2023-09-14 11:25:40.671358

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e2b1380db52'
down_revision: Union[str, None] = '807a35f4e8c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'author',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('author')
