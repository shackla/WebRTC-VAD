import wave
import contextlib
import os.path


maxVal = 20
totDuration = 0
for j in range(0, maxVal):
    chunk = 'chunk-0%s.wav' % j
    if os.path.isfile(chunk):
        print('Analysing Chunk No.: %s' % chunk)
        with contextlib.closing(wave.open(chunk, 'rb')) as wf:
            frames = wf.getnframes()
            rate = wf.getframerate()
            duration = frames/float(rate)
            os.remove(chunk)
            if duration > 0.5:
                print('Speech in Segment: %s' % duration)
                totDuration = totDuration + duration
                print('Duration of Speech: %s' % totDuration)

    else:
        break
