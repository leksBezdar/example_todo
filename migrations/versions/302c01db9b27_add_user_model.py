"""Add user model

Revision ID: 302c01db9b27
Revises: 86e72b0cc52c
Create Date: 2024-01-15 19:20:32.941902

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '302c01db9b27'
down_revision: Union[str, None] = '86e72b0cc52c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
