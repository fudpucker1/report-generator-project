"""
Squadron Activity Report Generator

This script demonstrates how to use the report_functions module
to generate a comprehensive squadron activity report.

Students will build this step-by-step in the assignment.
"""

import report_functions as rf


def generate_squadron_report(squadron_code, output_file):
    """
    Generates a comprehensive activity report for a specific squadron.

    Args:
        squadron_code (str): Squadron identifier (e.g., 'VFA-41')
        output_file (str): Path to save the report
    """
    # TODO: PART 1 - Load the data files
    aircraft_data = rf.read_csv_file("../data/aircraft.csv")
    flight_data = rf.read_csv_file("../data/flight_logs.csv")
    pilot_data = rf.read_csv_file("../data/pilots.csv")
    pass

    # TODO: PART 2 - Filter data for the specified squadron
    aircraft_filtered = rf.filter_by_field(aircraft_data, "squadron", squadron_code)
    pilot_filtered = rf.filter_by_field(pilot_data, "squadron", squadron_code)
    pass

    # TODO: PART 3 - Get flights for squadron pilots
    pilot_flights = rf.join_data(flight_data, pilot_filtered, "pilot_id","pilot_id")
    combined_flight = rf.join_data(pilot_flights, aircraft_filtered, "aircraft_id", "aircraft_id")

    pass

    # TODO: PART 4 - Calculate statistics
    flight_type_stats = []

    flight_types = rf.get_unique_values(combined_flight, "mission_type")
    total_fuel_overal = rf.calculate_total(combined_flight, "fuel_used_lbs")
    total_hours_flown = rf.calculate_total(combined_flight, "duration_hours")
    average_mission_duration_overall = rf.calculate_average(combined_flight, "duration_hours")

    for mission_type in flight_types:
        matching_flights = rf.filter_by_field(combined_flight, "mission_type", mission_type)
        flight_type_stats.append({mission_type: rf.count_records(matching_flights)})

    pass

    # TODO: PART 5 - Build the report content
    content = f"{rf.format_header('Overall Stats')} \n \n"
    content += f"Total Flights Flown: {len(combined_flight)} \n"
    content += f"Total Hours Flown: {total_hours_flown} \n"
    content += f"Total Fuel Used: {total_fuel_overal} \n"
    content += f"Average Mission Duration: {average_mission_duration_overall} \n"
    content += f"\n{rf.format_header('Mission Types')} \n \n"

    for entry in flight_type_stats:
        for mission, count in entry.items():
            content += f"{mission}: {count} \n"


    pass

    # TODO: PART 6 - Write the report to file
    rf.write_report_to_file(output_file, content)
    pass


# Main execution
if __name__ == '__main__':
    # TODO: Students will customize this to generate reports for different squadrons
    print("Generating squadron activity reports...")

    # Example: Generate report for VFA-41 (Black Aces)
    generate_squadron_report('VFA-41', '../reports/vfa-41-report.txt')
    generate_squadron_report('VFA-25', '../reports/vfa-25-report.txt')
    generate_squadron_report('VFA-154', '../reports/vfa-154-report.txt')
    generate_squadron_report('VFA-113', '../reports/vfa-113-report.txt')

    print("\nImplement the function above, then uncomment to test!")
