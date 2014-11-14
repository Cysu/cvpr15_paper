from matplotlib import rc
rc('font', family='serif', size=12)
rc('text', usetex=True)

import daft

pgm = daft.PGM([4, 3.25], origin=[-1.75, -1.75])
pgm.add_node(daft.Node('x', r'$x_n$', 0, 0, observed=True))
pgm.add_node(daft.Node('y', r'$y_n$', 1, 0))
pgm.add_node(daft.Node('z', r'$z_n$', 0, -1))
pgm.add_node(daft.Node('y_tilde', r'$\tilde{y}_n$', 1, -1, observed=True))
pgm.add_node(daft.Node('theta_1', r'$\theta_1$', 1, 1))
pgm.add_node(daft.Node('theta_2', r'$\theta_2$', -1, -1))
pgm.add_plate(daft.Plate([-0.5, -1.5, 2, 2], label=r'$N$', label_offset=[100, 5]))
pgm.add_edge('x', 'y')
pgm.add_edge('x', 'z')
pgm.add_edge('y', 'y_tilde')
pgm.add_edge('z', 'y_tilde')
pgm.add_edge('theta_1', 'y')
pgm.add_edge('theta_2', 'z')
pgm.render()
pgm.figure.savefig('pgm.pdf')