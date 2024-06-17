"""add Auth

Revision ID: d275b6b12635
Revises: b35e201602e7
Create Date: 2024-06-17 18:05:51.108626

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd275b6b12635'
down_revision: Union[str, None] = 'b35e201602e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('auth', sa.Column('username', sa.String(length=50), nullable=False))
    op.drop_column('auth', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('auth', sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.drop_column('auth', 'username')
    # ### end Alembic commands ###
