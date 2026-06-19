class Evaluator:
    def __init__(self, model, benchmark='humaneval'):
        self.model = model
        self.benchmark = benchmark
    
    def run(self, n_samples=100):
        """Run evaluation and return pass@k scores."""
        return {'pass@1': 0.0, 'pass@10': 0.0, 'pass@100': 0.0}
