"""create izdavac table

Revision ID: 1208f1e43cb7
Revises: 9e2b1380db52
Create Date: 2023-09-14 11:50:11.115896

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1208f1e43cb7'
down_revision: Union[str, None] = '9e2b1380db52'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'izdavac',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('ime', sa.String(length=255), nullable=False),
        sa.Column('adresa', sa.String(length=255)),
        sa.Column('telefon', sa.String(length=20)),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('izdavac')
