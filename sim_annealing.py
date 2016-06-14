def simulated_annealing(s_0, s_len, b_0, M=1000):
  s_t = s_0
  for t in range(s_len):
    s_t = last_s
    for i in range(M):
      # Choose a new candidate state s randomly (local to s_t - e.g. "bitflip")
      # "bitflip" -> randomly choose a feature of s_t and flip the value
      # calc difference in cost DE = E_s - E_s_t (DE > 0 -> Higher cost (worst))
      # switch s_t to s with probability W_s_t_to_s = 1 / (1+exp(b, DE))
      # (otherwise keep the old state s_t)
    b_t = r * b_t_-_1  # (r > 1 -> increase of b)
