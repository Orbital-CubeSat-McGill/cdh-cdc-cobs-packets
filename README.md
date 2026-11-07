# cdh-cdc-cobs-packets
| Field | Value |
|---|---|
| Description | Packet construction for Serial over USB comms for Green Bear flight 1. |
| Deployment date | 2026-11-08 |
| Author | Jacob Sauvé, OCS2 SW lead |
| State | In progress |

## What the project is
This project is used by both the BeagleBone Green fitted with its Ion0 hat, as well as the Red Board with its Green Board hat, in order to encode and decode packets sent over USB using pyserial.
It uses Consistent-Overhead Byte-Stuffing (COBS) to terminate frames consistently without adding too many excess bytes.
It uses CRC-16 as a "checksum" to flag corruption over USB CDC AMC communications between the BeagleBone and the Red Board.

## How to run it 
[***TO-DO***]

## What it does
| Inputs | Outputs |
|---|---|
|Raw data frame (telemetry data)|Header + COBS-packed frame + CRC-16|

## Some useful resources

* [Wikipedia article on COBS](https://en.wikipedia.org/wiki/Consistent_Overhead_Byte_Stuffing)
* [CRC-16 calculator and explanation](https://www.rfwireless-world.com/calculators/crc16-calculator-and-formula) (we use CCITT-FALSE)
