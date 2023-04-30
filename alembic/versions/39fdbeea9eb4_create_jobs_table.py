"""create jobs table

Revision ID: 39fdbeea9eb4
Revises: 
Create Date: 2023-05-01 00:32:35.540541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39fdbeea9eb4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'jobs',
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("title", sa.String, unique=True, index=True),
        sa.Column("company", sa.String, index=True),
        sa.Column("location", sa.String, index=True),
        sa.Column("posted_date", sa.String, index=True),
        sa.Column("description", sa.String, index=True),
        sa.Column("skills", sa.String, index=True)
    )


def downgrade() -> None:
    op.drop_table("jobs")
