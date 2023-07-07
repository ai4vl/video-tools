from pathlib import Path

from video_tools.aggregate import Aggregator


def test_aggregator():
    data_folder = Path(f"{__file__}").parent / "data"
    source_folder = data_folder
    output_folder = data_folder / "output"
    aggregator = Aggregator(source_folder, output_folder, dry_run=True, seperator_frames=30)
    aggregator.run()
