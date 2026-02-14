from django.shortcuts import render
import math


def home(request):
    result = None

    if request.method == "POST":
        try:
            # Warehouse input
            warehouse_input = request.POST.get("warehouse")
            wx, wy = map(float, warehouse_input.split(","))
            warehouse = (wx, wy)

            # Locations input
            raw_locations = request.POST.get("locations")
            points = []

            for item in raw_locations.split(";"):
                x, y = map(float, item.split(","))
                points.append((x, y))

            current = warehouse
            route = []
            total_distance = 0

            while points:
                nearest = min(points, key=lambda p: math.dist(current, p))
                total_distance += math.dist(current, nearest)
                route.append(nearest)
                current = nearest
                points.remove(nearest)

            # Full route including warehouse
            full_route = [warehouse] + route

            # Arrow formatted route string
            route_string = " → ".join([f"({x}, {y})" for x, y in full_route])

            result = {
                "warehouse": warehouse,
                "route": route_string,
                "distance": round(total_distance, 2)
            }

        except Exception:
            result = {
                "warehouse": None,
                "route": "Invalid input format. Please use x,y;x,y format.",
                "distance": 0
            }

    return render(request, "home.html", {"result": result})
