
import meerkat as mk

dp = mk.get("imagenette")
dp_pivot = mk.gui.Pivot(dp)

# TODO: do the embedding so you can actually match 
# if 
# dp = mk.embed(

# )
# dp.write("")

match: mk.gui.Component = mk.gui.Match(
    dp_pivot, 
    against="img",
    col="label"
)

sorted_box = mk.sort(dp_pivot, by=match.col, ascending=False)

gallery = mk.gui.Gallery(
    sorted_box,
    main_column="img",
    tag_columns=["label"],
)

mk.gui.start()
mk.gui.Interface(
    components=[match, gallery]
).launch()