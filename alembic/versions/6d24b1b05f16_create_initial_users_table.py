"""Create initial users table

Revision ID: 6d24b1b05f16
Revises: 
Create Date: 2016-04-20 20:50:25.560979

"""

# revision identifiers, used by Alembic.
revision = '6d24b1b05f16'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
            'users',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('is_admin', sa.Boolean, nullable=False, default=False),
            sa.Column('email', sa.Unicode(length=100), nullable=False, unique=True),
            sa.Column('password_hash', sa.String, nullable=False),
            sa.Column('salt', sa.String, nullable=False),
    )


def downgrade():
    op.drop_table('users')

