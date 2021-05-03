import neat

import visualize

class NeatAgent():
    def __init__(self, config_file):
        self.config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet,
                                  neat.DefaultStagnation, config_file)

        self.population = neat.Population(self.config)
        self.population.add_reporter(neat.StdOutReporter(True))
        self.stats = neat.StatisticsReporter()
        self.population.add_reporter(self.stats)
        self.population.add_reporter(neat.Checkpointer(generation_interval= 5,filename_prefix="neat-checkpoint-"))

    def run(self, eval_genomes, generations):
        winner = self.population.run(eval_genomes, generations)
        return winner

    def visualize(self, genome):
        visualize.draw_net(self.config, genome, True, node_names={})
        visualize.plot_stats(self.stats, ylog=False, view=True)
        visualize.plot_species(self.stats, view=True)