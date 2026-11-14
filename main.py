import os
from pathlib import Path

POEM = """At 6:12 the kettle clicks off.
My brother's text waits beside the sink:
Can you come?
I type yes, erase it,
type I can't, erase that too.
Rain threads the fire escape.
The blue bowl dries upside down,
where he left it Sunday.

I ask a machine to help me answer.
It lays out three sentences,
clean as folded towels.
I take one, change the end:
After work. I'll bring the bowl—
the chipped one from our old kitchen,
the one he asks for when peaches
taste like the hospital spoon.

I send it. The reply arrives
while the kettle cools:
Thanks. Mom's asleep.
My words travel
on a sentence another mind held open.
I set my keys by the door.
The bowl waits, mouth to the dish rack.
I turn it up before I leave."""

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(POEM, encoding="utf-8")
