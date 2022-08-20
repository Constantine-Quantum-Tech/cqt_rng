
from ..base.post_processor import PostProcessor
from .von_neumann_pp import VonNeumannPP

class CQTPP(PostProcessor):
	def __init__(self, **kwargs):
		self.dep_seq_len = kwargs.get("dep_seq_len")
		if self.dep_seq_len is None:
			self.dep_seq_len = 1

	def postprocess(self, sample_1, sample_2):
		# if unbiased and dep_seq_len > 1:
		# new_bitstring = np.array([], dtype=np.int8)
		# for i in range(gen_len // dep_seq_len):
		# 	sub_s1 = sample_1[i * dep_seq_len:(i+1) * dep_seq_len]
		# 	sub_s2 = sample_2[i * dep_seq_len:(i+1) * dep_seq_len]
		# 	postprocess_output = VonNeumannPP().postprocess(sub_s1, sub_s2)
		# 	if np.size(postprocess_output):
		# 		new_bitstring = np.append(new_bitstring, np.array([postprocess_output[0]]))
		
		return super().postprocess(sample_1, sample_2)
