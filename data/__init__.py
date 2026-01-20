"""Package de données statiques du projet USSD."""

# Réexport pour compatibilité
from .ussd_menus import USSD_DATA
from .tarifs import (
    OFFRES,
    FRAIS_RETRAIT,
    FRAIS_TRANSFERT_MVOLA,
    FRAIS_TRANSFERT_AUTRES,
    YAS_MITSINJO_KITS,
    MBALIK_KITS,
    MBALIK_RECHARGES
)

__all__ = [
    'USSD_DATA',
    'OFFRES',
    'FRAIS_RETRAIT',
    'FRAIS_TRANSFERT_MVOLA',
    'FRAIS_TRANSFERT_AUTRES',
    'YAS_MITSINJO_KITS',
    'MBALIK_KITS',
    'MBALIK_RECHARGES'
]
