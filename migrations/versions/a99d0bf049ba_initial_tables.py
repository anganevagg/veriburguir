"""initial tables

Revision ID: a99d0bf049ba
Revises: 
Create Date: 2022-11-26 16:59:42.876435

"""
from alembic import op
from alembic.operations.ops import CreateForeignKeyOp, CreatePrimaryKeyOp
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a99d0bf049ba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
  burger_table = op.create_table('Burger',
    sa.Column("id", sa.Integer(), nullable=False),
    sa.Column("name", sa.String(50), nullable = False),
    sa.Column("price", sa.DECIMAL(2), nullable = False),
		sa.Column("selled", sa.Integer(), nullable = False),
    sa.PrimaryKeyConstraint("id")
  )
  order_table = op.create_table('Order',
    sa.Column("id", sa.Integer(), nullable=False),
		sa.Column("total", sa.DECIMAL(2)),
    sa.PrimaryKeyConstraint("id")
  )
  relation_table = op.create_table('burger_order', 
    sa.Column('order_id', sa.Integer(), sa.ForeignKey('Order.id')),
    sa.Column('burger_id', sa.Integer(), sa.ForeignKey('Burger.id'))
  )
def downgrade() -> None:
    pass
