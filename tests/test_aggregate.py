from pathlib import Path

from video_tools.aggregate import Aggregator


def test_aggregator():
    data_folder = Path(f"{__file__}").parent / "data"
    source_folder = data_folder
    output_folder = data_folder / "output"
    aggregator = Aggregator(source_folder, output_folder, dry_run=True, seperator_frames=30)
    input_matches = list(aggregator.search_for_input_matches())
    assert len(input_matches) == 4
    aggregations = list(aggregator.get_aggregations(input_matches))
    assert len(aggregations) == 2
    aggregator.run()
