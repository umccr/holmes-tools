# holmes-tools

Some python/bash tools that can be used against the Holmes
fingerprint database to help investigations/debug.

The difference with these tools is that they generally run directly
on the fingerprint bucket itself - so are not mediated by the
actual Holmes code.

Some of this functionality could perhaps find its way into the core
Holmes.

## `dump.py`

Execute (with production permissions)

`pipenv run python dump.py`

will dump the filename of every BAM that has been fingerprinted in Holmes
along with the date the fingerprint was last updated (which in general would
be the same as when it was created - though BAMs can be fingerprinted multiple
times and the fingerprint file will just be updated).

## `exists.py`

Execute (with production permissions)

`pipenv run python exists.py < (a list of BAM files)`

will consult the fingerprint database for every BAM file
given on stdin and print what the fingerprint path for that file would
be, and an indication of whether it currently exists.

The output is TSV file in the format

```text
(BAM file path)\t(Fingerprint path in S3)
(BAM file path)\t(Fingerprint path in S3)
(BAM file path)\t(Fingerprint path in S3)
(BAM file path)\t(Fingerprint path in S3)
```

where fingerprint path is an empty string if that fingerprint does not actually exist.
