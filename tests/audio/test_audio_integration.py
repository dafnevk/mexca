""" Test audio speaker id and voice feature integration classes and methods """

import json
import os
from mexca.audio.extraction import VoiceExtractor
from mexca.audio.integration import AudioIntegrator
from mexca.audio.identification import SpeakerIdentifier


class TestAudioIntegrator:
    integrator = AudioIntegrator(
        SpeakerIdentifier(),
        VoiceExtractor(time_step=0.04)
    )
    filepath = os.path.join('tests', 'test_files', 'test_eng_5_seconds.wav')

    with open(
        os.path.join('tests', 'reference_files', 'features_eng_5_seconds.json'), 'r', encoding="utf-8"
    ) as file:
        reference_features = json.loads(file.read())

    def test_integrate(self):
        annotated_features = self.integrator.apply(self.filepath, None)
        assert all(annotated_features['segment_id'] == self.reference_features['segment_id'])
