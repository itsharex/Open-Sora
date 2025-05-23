_base_ = ["image.py"]

# new config
grad_ckpt_settings = (100, 100)

plugin = "hybrid"
plugin_config = dict(
    tp_size=1,
    pp_size=1,
    sp_size=4,
    sequence_parallelism_mode="ring_attn",
    enable_sequence_parallelism=True,
    static_graph=True,
    zero_stage=2,
)

bucket_config = {
    "_delete_": True,
    "256px": {
        1: (1.0, 130),
        5: (1.0, 14),
        9: (1.0, 14),
        13: (1.0, 14),
        17: (1.0, 14),
        21: (1.0, 14),
        25: (1.0, 14),
        29: (1.0, 14),
        33: (1.0, 14),
        37: (1.0, 10),
        41: (1.0, 10),
        45: (1.0, 10),
        49: (1.0, 10),
        53: (1.0, 10),
        57: (1.0, 10),
        61: (1.0, 10),
        65: (1.0, 10),
        73: (1.0, 7),
        77: (1.0, 7),
        81: (1.0, 7),
        85: (1.0, 7),
        89: (1.0, 7),
        93: (1.0, 7),
        97: (1.0, 7),
        101: (1.0, 6),
        105: (1.0, 6),
        109: (1.0, 6),
        113: (1.0, 6),
        117: (1.0, 6),
        121: (1.0, 6),
        125: (1.0, 6),
        129: (1.0, 6),
    },
    "768px": {
        1: (1.0, 38),
        5: (1.0, 6),
        9: (1.0, 6),
        13: (1.0, 6),
        17: (1.0, 6),
        21: (1.0, 6),
        25: (1.0, 6),
        29: (1.0, 6),
        33: (1.0, 6),
        37: (1.0, 4),
        41: (1.0, 4),
        45: (1.0, 4),
        49: (1.0, 4),
        53: (1.0, 4),
        57: (1.0, 4),
        61: (1.0, 4),
        65: (1.0, 4),
        69: (1.0, 3),
        73: (1.0, 3),
        77: (1.0, 3),
        81: (1.0, 3),
        85: (1.0, 3),
        89: (1.0, 3),
        93: (1.0, 3),
        97: (1.0, 3),
        101: (1.0, 2),
        105: (1.0, 2),
        109: (1.0, 2),
        113: (1.0, 2),
        117: (1.0, 2),
        121: (1.0, 2),
        125: (1.0, 2),
        129: (1.0, 2),
    },
}

model = dict(grad_ckpt_settings=grad_ckpt_settings)
lr = 5e-5
optim = dict(lr=lr)
ckpt_every = 200
keep_n_latest = 20
