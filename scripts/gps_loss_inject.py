from pymavlink import mavutil
import time

print("Connecting to SITL...")
master = mavutil.mavlink_connection('udp:127.0.0.1:14550')
master.wait_heartbeat()
print(f"Connected ✅ — system {master.target_system} component {master.target_component}")

# Wait before injecting — give the mission time to start
DELAY = 60  # seconds into flight before GPS block
print(f"Waiting {DELAY}s before injecting GPS loss...")
time.sleep(DELAY)

print("🔴 Injecting GPS block now...")
master.mav.param_set_send(
    master.target_system,
    master.target_component,
    b'SIM_GPS_BLOCK',
    1,
    mavutil.mavlink.MAV_PARAM_TYPE_INT32
)
print("GPS blocked ✅ — watch for EKF warnings and failsafe in QGC")

# Hold for 60s then restore
time.sleep(60)
print("🟢 Restoring GPS...")
master.mav.param_set_send(
    master.target_system,
    master.target_component,
    b'SIM_GPS_BLOCK',
    0,
    mavutil.mavlink.MAV_PARAM_TYPE_INT32
)
print("GPS restored ✅")
