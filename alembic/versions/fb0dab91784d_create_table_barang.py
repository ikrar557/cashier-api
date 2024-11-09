"""create table barang

Revision ID: fb0dab91784d
Revises: 
Create Date: 2024-11-09 20:57:03.096591

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'fb0dab91784d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('barang',
                    sa.Column('nobarcode', sa.String, primary_key=True),
                    sa.Column('nama', sa.String),
                    sa.Column('harga', sa.Integer),
                    sa.Column('stok', sa.Integer))


def downgrade() -> None:
    op.drop_table('barang')
