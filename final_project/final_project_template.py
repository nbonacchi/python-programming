#!/usr/bin/env python
# @File: final_project\final_project_template.py
# @Author: Niccolo' Bonacchi (@nbonacchi)
# @Date: Wednesday, January 22nd 2025, 7:16:58 pm
"""
    Example implementation stubs for the final project
"""
import matplotlib.pyplot as plt


def read_data(filename: str) -> dict: ...


# Statistics
def calculate_mean(values: list) -> float: ...


def calculate_standard_deviation(values: list, mean: float) -> float: ...


def calculate_quartiles(values: list) -> tuple: ...


# Relationship statistics
def calculate_covariance(values_x: list, mean_x: float, values_y: list, mean_y: float) -> float: ...


def calculate_correlation(covariance: float, std_x: float, std_y: float) -> float: ...


# Use
def display_statistics(data: dict) -> None: ...


def display_relationship_statistics(data: dict) -> None: ...


# Plot
def plot_relationship(x: list, y: list, x_label: str, y_label: str, correlation: float) -> None: ...


# Organize aand execute the code
def main() -> None: ...


if __name__ == "__main__":
    main()
