#!/usr/bin/env python3

import asyncio

from grpc import Channel
from protobuf.DotaService_grpc import DotaServiceStub
from protobuf.DotaService_pb2 import Action
from protobuf.DotaService_pb2 import Config


async def main():
    # Connect to the DotaService.
    env = DotaServiceStub(Channel('127.0.0.1', 13337))

    # Get the initial observation.
    observation = await env.reset(Config())
    for i in range(8):
        # Sample an action from the action protobuf
        action = Action.MoveToLocation(x=2, y=2, z=2)
        # Take an action, returning the resulting observation.
        observation = await env.step(action)

if __name__ == '__main__':
    asyncio.run(main())
