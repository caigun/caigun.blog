## Evaluation Results

Experiment Configuration:

Pretrained Hubert from Wesper + Our model,
trained on _Librilight-medium_ + _Librilight-small_.

#### LibriTTS-Test-short _740 subset_ (3-8s)
| Category  | WER Mean (%) | WER Std Dev (%) |
|-----------|--------------|-----------------|
| GT        | 2.9330       | 5.7240          |
| Generated | 5.0120       | 10.8880         |
| Source    | 5.6140       | 10.6480         |
| Wesper    |              |                 |

##### Generated Samples:
| No | GT| Generated | Source | Wesper |
|----|---|-----------|--------|--------|
|1|<audio controls><source src="/whisper2speech/sample/gt/28.wav" type="audio/wav"></audio>|<audio controls><source src="/whisper2speech/sample/recon/28.wav" type="audio/wav"></audio>|<audio controls><source src="/whisper2speech/sample/source/28.wav" type="audio/wav"></audio>|<audio controls><source src="/whisper2speech/sample/wesper/28.wav" type="audio/wav"></audio>|

---------------

#### LibriTTS-Test-long _690 subset_ (>8s)
| Category  | WER Mean (%) | WER Std Dev (%) |
|-----------|--------------|-----------------|
| GT        | 2.7150       | 4.0250          |
| Generated | 5.5500       | 14.8500         |
| Source    | 5.1930       | 11.5320         |
| Wesper    | 12.6560      | 14.9150         |

D:\GitHub\caigun.github.io\whisper2speech\eval.md