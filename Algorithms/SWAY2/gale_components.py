"""
    This file is part of GALE,
    Copyright Joe Krall, 2014.

    GALE is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    GALE is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with GALE.  If not, see <http://www.gnu.org/licenses/>.
"""

from Fastmap.Slurp import *
from Fastmap.Moo import *
from jmoo_individual import *


def gale_nm_WHERE(problem, population, configuration, values_to_be_passed):
    "The Core method behind GALE"

    # for pop in population:
    #     assert(pop.generation_number == 0), "Generation has to be 0"

    # Compile population into table form used by WHERE
    t = slurp([[x for x in row.decisionValues] + ["?" for y in problem.objectives] for row in population],
              problem.buildHeader().split(","))

    # Initialize some parameters for WHERE
    The.allowDomination = True
    The.alpha = 1
    for i, row in enumerate(t.rows):
        row.evaluated = False

    # Run WHERE
    m = Moo(problem, t, len(t.rows), N=1).divide(minnie=rstop(t))

    # Organizing
    NDLeafs = m.nonPrunedLeaves()  # The surviving non-dominated leafs
    allLeafs = m.nonPrunedLeaves() + m.prunedLeaves()  # All of the leafs

    # After mutation: Check how many rows were actually evaluated
    numEval = 0
    for leaf in allLeafs:
        for row in leaf.table.rows:
            if row.evaluated:
                numEval += 1

    return NDLeafs, numEval


def gale_nm_Mutate(problem, NDLeafs, configuration):
    #################
    # Mutation Phase
    #################

    number_of_evaluation = 0
    # After mutation; Convert back to JMOO Data Structures
    population = []
    for leaf in NDLeafs:
        for row in leaf.table.rows:
            if row.evaluated:
                population.append(jmoo_individual(problem, [x for x in row.cells[:len(problem.decisions)]],
                                                  [x for x in row.cells[len(problem.decisions):]]))
                number_of_evaluation += 1
            else:
                member = jmoo_individual(problem, [x for x in row.cells[:len(problem.decisions)]], None)
                member.evaluate()
                population.append(member)
                number_of_evaluation += 1

    if number_of_evaluation < 2:
        while True:
            from random import randint
            index = randint(0, len(population) - 1)
            if population[index].valid is not True:
                population[index].evaluate()
                number_of_evaluation +=1
                break

    if number_of_evaluation == 0:
        return population, 0
    else:
        return population, number_of_evaluation


def gale_nm_Regen(problem, unusedslot, mutants, configuration):
    howMany = configuration["Universal"]["Population_Size"]
    # Generate random individuals
    population = []
    for i in range(howMany):
        population.append(jmoo_individual(problem, problem.generateInput(), None))
    
    return population, 0
