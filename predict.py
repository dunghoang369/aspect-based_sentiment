# Use pretrained SpanModel weights for prediction
import json
import sys
sys.path.append("aste")
from pathlib import Path
from data_utils import Data, Sentence, SplitEnum
from wrapper import SpanModel
import subprocess


if __name__ == "__main__":
    model_dir = "xlm_coref_15_max_span_width"
    def predict_sentence(text: str, model: SpanModel) -> Sentence:
        path_in = "temp_in.txt"
        path_out = "temp_out.txt"
        sent = Sentence(tokens=text.split(), triples=[], pos=[], is_labeled=False, weight=1, id=0)
        data = Data(root=Path(), data_split=SplitEnum.test, sentences=[sent])
        data.save_to_path(path_in)
        model.predict(path_in, path_out)
        data = Data.load_from_full_path(path_out)
        return data.sentences[0]

    texts = ["cần thêm các gói cước cho các dịch vụ combo tiktok youtube EVENT",
            "cần có nhiều khuyến mãi bằng thẻ cào hơn",
            "cần nhanh chóng nâng cấp lên 5g nữa là ok ạ",
            "chăm sóc khách hàng tốt hơn",
            "mong bobi khuyến mãi tốt hơn nữa"]

    for text in texts:
        model = SpanModel(save_dir=model_dir, random_seed=0)
        sent = predict_sentence(text, model)
        result = []
        for t in sent.triples:
            target = " ".join(sent.tokens[t.t_start:t.t_end+1])
            opinion = " ".join(sent.tokens[t.o_start:t.o_end+1])
            tmp = "" + target + "----" + opinion
            result.append(tmp)

        with open("test_abs.txt", "a") as f:
            f.write(text)
            f.write("\t")
            f.write(str(result))
            f.write("\n")

    subprocess.run("rm temp_in.txt temp_out.txt", shell=True)

