"""add foreign key to Review

Revision ID: 590c37ba0d3a
Revises: 7c7b738f8aae
Create Date: 2024-06-28 20:35:19.092467

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite


# revision identifiers, used by Alembic.
revision = '590c37ba0d3a'
down_revision = '7c7b738f8aae'
branch_labels = None
depends_on = None


def upgrade():
    # Use batch mode to alter the table
    with op.batch_alter_table('reviews', recreate='always') as batch_op:
        batch_op.create_foreign_key(
            'fk_reviews_employee_id_employees', 'employees', ['employee_id'], ['id'])

def downgrade():
    # Use batch mode to alter the table
    with op.batch_alter_table('reviews', recreate='always') as batch_op:
        batch_op.drop_constraint('fk_reviews_employee_id_employees', type_='foreignkey')
