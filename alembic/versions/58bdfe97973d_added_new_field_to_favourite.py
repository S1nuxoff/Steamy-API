"""Added new field to Favourite

Revision ID: 58bdfe97973d
Revises: 
Create Date: 2024-10-30 04:01:12.326139

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '58bdfe97973d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Преобразование столбца с использованием `USING` для указания нового типа
    op.alter_column(
        'currencies',
        'time',
        existing_type=sa.VARCHAR(),
        type_=sa.DateTime(timezone=True),
        existing_nullable=False,
        postgresql_using="time::timestamp with time zone"
    )

def downgrade() -> None:
    # Возвращаем тип данных к исходному значению с использованием `USING`
    op.alter_column(
        'currencies',
        'time',
        existing_type=sa.DateTime(timezone=True),
        type_=sa.VARCHAR(),
        existing_nullable=False,
        postgresql_using="time::text"
    )
