""" Test speaker identification classes and methods """

import json
import itertools
import os
import pytest
from pyannote.core import Annotation
from mexca.audio.speaker_id import SpeakerIdentifier

class TestSpeakerIdentifier:
    detector = SpeakerIdentifier()
    filepath = os.path.join(
        'tests', 'audio_files', 'test_audio_5_seconds.wav'
    )
    with open(os.path.join(
            'tests', 'reference_files', 'reference_audio_5_seconds.json'
        ), 'r') as file:
        ref_speakers = Annotation.from_json(json.loads(file.read()))

    def test_apply(self):
        speakers = self.detector.apply(self.filepath)
        track_pairs = itertools.zip_longest(
            speakers.itertracks(yield_label=True),
            self.ref_speakers.itertracks(yield_label=True)
        )
        for track, ref_track in track_pairs:
            assert pytest.approx(track[0].start, rel=1e-2) == ref_track[0].start
            assert pytest.approx(track[0].end, rel=1e-2) == ref_track[0].end
            assert track[1] == ref_track[1]
            assert track[2] == ref_track[2]