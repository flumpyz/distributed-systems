"""initial

Revision ID: a175d6389838
Revises: 
Create Date: 2022-11-13 19:42:02.873398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a175d6389838'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('links',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_links_id'), 'links', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_links_id'), table_name='links')
    op.drop_table('links')
