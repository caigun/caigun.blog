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
| Wesper    | 7.7174       | 12.2524         |

##### Generated Samples:
Here's the expanded table with the labels provided:

| No | GT | Generated | Source | Wesper |
|----|----|-----------|--------|--------|
| 28 | <audio controls><source src="/whisper2speech/sample/gt/28.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/recon/28.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/source/28.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/wesper/28.wav" type="audio/wav"></audio> |
| 61 | <audio controls><source src="/whisper2speech/sample/gt/61.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/recon/61.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/source/61.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/wesper/61.wav" type="audio/wav"></audio> |
| 117 | <audio controls><source src="/whisper2speech/sample/gt/117.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/recon/117.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/source/117.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/wesper/117.wav" type="audio/wav"></audio> |
| 148 | <audio controls><source src="/whisper2speech/sample/gt/148.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/recon/148.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/source/148.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/wesper/148.wav" type="audio/wav"></audio> |
| 270 | <audio controls><source src="/whisper2speech/sample/gt/270.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/recon/270.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/source/270.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/wesper/270.wav" type="audio/wav"></audio> |
| 394 | <audio controls><source src="/whisper2speech/sample/gt/394.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/recon/394.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/source/394.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/wesper/394.wav" type="audio/wav"></audio> |
| 489 | <audio controls><source src="/whisper2speech/sample/gt/489.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/recon/489.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/source/489.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/wesper/489.wav" type="audio/wav"></audio> |
| 561 | <audio controls><source src="/whisper2speech/sample/gt/561.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/recon/561.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/source/561.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/wesper/561.wav" type="audio/wav"></audio> |
| 617 | <audio controls><source src="/whisper2speech/sample/gt/617.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/recon/617.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/source/617.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/sample/wesper/617.wav" type="audio/wav"></audio> |

---------------

#### LibriTTS-Test-long _690 subset_ (>8s)
| Category  | WER Mean (%) | WER Std Dev (%) |
|-----------|--------------|-----------------|
| GT        | 2.7150       | 4.0250          |
| Generated | 5.5500       | 14.8500         |
| Source    | 5.1930       | 11.5320         |
| Wesper    | 12.6560      | 14.9150         |

| No | GT | Generated | Source | Wesper |
|----|----|-----------|--------|--------|
| 22  | <audio controls><source src="/whisper2speech/long/gt/22.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/recon/22.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/source/22.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/wesper/22.wav" type="audio/wav"></audio> |
| 299 | <audio controls><source src="/whisper2speech/long/gt/299.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/recon/299.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/source/299.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/wesper/299.wav" type="audio/wav"></audio> |
| 366 | <audio controls><source src="/whisper2speech/long/gt/366.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/recon/366.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/source/366.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/wesper/366.wav" type="audio/wav"></audio> |
| 389 | <audio controls><source src="/whisper2speech/long/gt/389.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/recon/389.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/source/389.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/wesper/389.wav" type="audio/wav"></audio> |
| 449 | <audio controls><source src="/whisper2speech/long/gt/449.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/recon/449.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/source/449.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/wesper/449.wav" type="audio/wav"></audio> |
| 524 | <audio controls><source src="/whisper2speech/long/gt/524.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/recon/524.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/source/524.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/wesper/524.wav" type="audio/wav"></audio> |
| 572 | <audio controls><source src="/whisper2speech/long/gt/572.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/recon/572.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/source/572.wav" type="audio/wav"></audio> | <audio controls><source src="/whisper2speech/long/wesper/572.wav" type="audio/wav"></audio> |
