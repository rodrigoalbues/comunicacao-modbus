from pyModbusTCP.client import ModbusClient

print("=" * 60)
comm_config = ModbusClient(
    host="192.168.0.10",
    port=502,
    unit_id=1,
    timeout=500.0,
    auto_open=True,
    auto_close=True,
)
v_lidas = comm_config.read_input_registers(0, 10)
print(f"Variáveis lidas: {v_lidas}")
v_escritas = comm_config.write_multiple_registers(0, [1, 2, 3])
print(f"Variáveis foram escritas: {v_escritas}")
print("=" * 60)
