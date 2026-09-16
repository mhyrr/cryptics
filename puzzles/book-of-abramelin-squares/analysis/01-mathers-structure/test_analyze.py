import unittest
from analyze import constrain, generators, masked_check, validate


class StructureTests(unittest.TestCase):
    def test_sator_calibration_and_unknown_center(self):
        grid = list(map(list, ["SATOR", "AREPO", "TENET", "OPERA", "ROTAS"]))
        self.assertTrue(constrain(grid, "transpose_and_half_turn")["compatible"])
        grid[0][1] = None
        grid[2][2] = None
        result = constrain(grid, "transpose_and_half_turn")
        self.assertEqual(result["conditional_fills"], [{"row": 0, "column": 1, "letter": "A"}])
        self.assertEqual(result["free_orbits"], [[(2, 2)]])

    def test_conflicting_orbit_is_never_repaired(self):
        grid = [["A", "B", None], ["C", "D", None], [None, None, "E"]]
        result = constrain(grid, "transpose")
        self.assertFalse(result["compatible"])
        self.assertEqual(len(result["conflicts"]), 1)
        self.assertEqual(result["conditional_fills"], [])

    def test_generators_and_single_cell_corruption(self):
        grid = list(map(list, ["ABC", "BCA", "CAB"]))
        self.assertEqual(generators(grid)["fixed_cyclic_steps"], [1])
        grid[1][1] = "Z"
        self.assertEqual(generators(grid)["fixed_cyclic_steps"], [])
        grid = list(map(list, ["ABC", "BCD", "CDE"]))
        self.assertEqual(generators(grid)["boundary_affine_mod26"]["row_+1_column_+1"]["mismatches"], 0)
        grid[2][2] = None
        self.assertIsNone(generators(grid))

    def test_bad_shapes_and_cells_are_not_silently_normalized(self):
        for grid in ([["A", "B"], ["C"]], [["A", "?"], ["C", "D"]]):
            with self.assertRaises(ValueError):
                validate(grid)

    def test_masked_check_counts_wrong_hidden_answers(self):
        # Top row / left column are consistent but hidden bottom-right is wrong.
        result = masked_check([[list("AB"), list("BZ")]], "transpose_and_half_turn")
        self.assertEqual(result["predicted"], 1)
        self.assertEqual(result["wrong"], 1)
        self.assertEqual(result["rejected"], 0)


if __name__ == "__main__":
    unittest.main()
