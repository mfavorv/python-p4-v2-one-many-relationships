"""add foreign key to onboarding

Revision ID: 9c04950b23d4
Revises: 590c37ba0d3a
Create Date: 2024-06-28 20:52:08.814851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c04950b23d4'
down_revision = '590c37ba0d3a'
branch_labels = None
depends_on = None



def upgrade():
    # Use batch mode to alter the table
    with op.batch_alter_table('onboardings', recreate='always') as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'fk_onboardings_employee_id_employees', 'employees', ['employee_id'], ['id']
        )


def downgrade():
    # Use batch mode to alter the table
    with op.batch_alter_table('onboardings', recreate='always') as batch_op:
        batch_op.drop_constraint('fk_onboardings_employee_id_employees', type_='foreignkey')
        batch_op.drop_column('employee_id')