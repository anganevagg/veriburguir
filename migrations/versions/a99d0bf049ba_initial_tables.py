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
  item_table = op.create_table('Item',
    sa.Column("id", sa.Integer(), nullable=False),
    sa.Column("name", sa.String(50), nullable = False),
    sa.Column("price", sa.DECIMAL(5, 2), nullable = False),
    sa.Column("selled", sa.Integer(), nullable = False, default = 0),
    sa.PrimaryKeyConstraint("id")
  )
  order_table = op.create_table('Order',
    sa.Column("id", sa.Integer(), nullable=False),
    sa.Column("total", sa.DECIMAL(2)),
    sa.PrimaryKeyConstraint("id")
  )
  relation_table = op.create_table('order_item', 
    sa.Column('order_id', sa.Integer(), sa.ForeignKey('Order.id')),
    sa.Column('item_id', sa.Integer(), sa.ForeignKey('Item.id'))
  )
  op.bulk_insert(item_table, [
    {
      "name": "gajoPapas",
      "price": 12.43,
    },

    {
      "name": "veriMalteadaLog",
      "price": 10.5,
    }, 

    {
      "name": "frenchPapas",
      "price": 12.43,
    }, 

    {
      "name": "cebollAros",
      "price": 12.43,
    }, 
    
    {
      "name": "kidBurger",
      "price": 18.5,
    }, 

    {
      "name": "classicBurguer",
      "price": 20.5,
    }, 

    {
      "name": "cubanBurguer",
      "price": 23.5,
    }, 

    {
      "name": "supremeBurguer",
      "price": 30.5,
    },

    {
      "name": "burguer?",
      "price": 1.0,
    }, 

    
  ])
def downgrade() -> None:
  op.drop_table("order_item")
  op.drop_table("Item")
  op.drop_table("Order")
