"""initial migration

Revision ID: 9184b96d7afc
Revises: f6ab84a174b8
Create Date: 2024-06-14 18:47:23.121160

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9184b96d7afc'
down_revision: Union[str, None] = 'f6ab84a174b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('lastname', sa.String(length=50), nullable=False))
    op.add_column('users', sa.Column('chat_id', sa.Integer(), nullable=False))
    op.add_column('users', sa.Column('language_code', sa.String(length=10), nullable=False))
    op.create_unique_constraint(None, 'users', ['chat_id'])
    op.create_foreign_key(None, 'users', 'users', ['chat_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'language_code')
    op.drop_column('users', 'chat_id')
    op.drop_column('users', 'lastname')
    # ### end Alembic commands ###