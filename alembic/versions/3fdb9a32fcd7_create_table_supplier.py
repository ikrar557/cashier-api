"""create table supplier

Revision ID: 3fdb9a32fcd7
Revises: fb0dab91784d
Create Date: 2024-11-09 20:59:53.131961

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3fdb9a32fcd7'
down_revision: Union[str, None] = 'fb0dab91784d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'supplier',
                    sa.Column('idsup', sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column('nama', sa.String),
                    sa.Column('alamat', sa.String),
                    sa.Column('nohp', sa.String))

def downgrade() -> None:
    op.drop_table('supplier')

