# intensity2rgb.py
# Copyright (c) 2026 Paolo Corradeghini - 3DMetrica. Licenza MIT (vedi LICENSE).
# https://github.com/3dmetrica/CloudCompareOnDemand
#
# Script per il Python plugin di CloudCompare (pycc).
# Su tutte le nuvole selezionate (o su tutte quelle nel DB Tree, se non
# hai selezionato nulla) spegne lo scalar field e accende i colori RGB.
# Le nuvole senza RGB vengono lasciate come sono e segnalate in console.

import pycc

CC = pycc.GetInstance()


def is_point_cloud(obj):
    try:
        return obj.isKindOf(pycc.CC_TYPES.POINT_CLOUD)
    except Exception:
        return hasattr(obj, "hasColors") and hasattr(obj, "showSF")


def collect_clouds(obj, out):
    """Raccoglie le nuvole anche dentro i gruppi creati all'import (es. E57)."""
    if is_point_cloud(obj):
        out.append(obj)
    for i in range(obj.getChildrenNumber()):
        collect_clouds(obj.getChild(i), out)


roots = CC.getSelectedEntities()
if not roots:
    roots = [CC.dbRootObject()]

clouds = []
for r in roots:
    collect_clouds(r, clouds)

done, no_rgb = 0, []
for cloud in clouds:
    if cloud.hasColors():
        cloud.showSF(False)
        cloud.showColors(True)
        done += 1
    else:
        no_rgb.append(cloud.getName())

CC.redrawAll()

print(f"RGB attivato su {done} nuvole.")
if no_rgb:
    print("Senza colori RGB (lasciate invariate):")
    for name in no_rgb:
        print("  -", name)