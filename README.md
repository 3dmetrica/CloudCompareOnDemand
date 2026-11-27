# CloudCompare On Demand

Script Python usati negli episodi di **CloudCompare On Demand**, la serie di 3DMetrica su CloudCompare.
Ogni script ha la sua cartella, con il link al video in cui lo uso.

*English below.*

| Script | Cosa fa | Episodio |
|---|---|---|
| [intensity2rgb](intensity2rgb/intensity2rgb.py) | Passa da Intensity a RGB su tutte le nuvole in un colpo | CCD_II_002 · [video](https://youtu.be/WjwTW9cZvAw) |

## intensity2rgb.py

Quando importi in CloudCompare molte scansioni laser (per esempio da un file E57), le vedi tutte colorate con il campo scalare *Intensity*, anche se hanno i colori RGB.
Lo script spegne la visualizzazione dello scalar field e accende i colori RGB:

- sulle nuvole selezionate nel *DB Tree*;
- se non hai selezionato nulla, su tutte le nuvole del *DB Tree*, anche dentro i gruppi creati all'import.

Le nuvole senza RGB restano come sono e lo script te le elenca nella *Console*.
Cambia solo la visualizzazione: i dati non vengono toccati e l'intensità resta disponibile.

### Cosa ti serve

- CloudCompare con il **Python plugin** (PythonRuntime). Nel video uso la versione stabile 2.13.2 per Windows: nell'installer l'opzione del Python plugin va spuntata, altrimenti non viene installato.
- All'avvio di CloudCompare controlla nella *Console* che il plugin si carichi senza righe rosse. Se non si carica, disinstalla e reinstalla CloudCompare con l'opzione spuntata.

### Come si usa

1. Scarica `intensity2rgb.py`.
2. In CloudCompare seleziona le nuvole su cui vuoi lavorare, oppure non selezionare nulla per lavorare su tutte.
3. Menu *Plugins* → *Python Plugin* → *File Runner*, scegli il file e premi *Run*.
4. Nella *Console* trovi quante nuvole sono passate all'RGB e quali non hanno i colori.

Documentazione del Python plugin: https://tmontaigu.github.io/CloudCompare-PythonRuntime

---

## English

Python scripts used in the episodes of **CloudCompare On Demand**, the 3DMetrica series on CloudCompare (videos in Italian, with English subtitles).

### intensity2rgb.py

When you import many laser scans into CloudCompare (for example from an E57 file), they all show up coloured by the *Intensity* scalar field, even if they have RGB colours.
The script turns off the scalar field display and turns on the RGB colours:

- on the clouds selected in the *DB Tree*;
- if nothing is selected, on every cloud in the *DB Tree*, including those inside the groups created on import.

Clouds without RGB are left as they are and listed in the *Console*.
It only changes the display: the data is not modified and the intensity is still available.

**Requirements:** CloudCompare with the **Python plugin** (PythonRuntime). In the video I use the stable 2.13.2 release for Windows: the Python plugin option must be ticked in the installer, otherwise it is not installed.

**How to use it:** select the clouds (or nothing, to work on all of them), then *Plugins* → *Python Plugin* → *File Runner*, choose `intensity2rgb.py` and press *Run*.

Plugin documentation: https://tmontaigu.github.io/CloudCompare-PythonRuntime

---

Licenza / License: [MIT](LICENSE) · Paolo Corradeghini, [3DMetrica](https://www.3dmetrica.it)
