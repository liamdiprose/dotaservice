#!/usr/bin/env python3

import asyncio

from grpclib.client import Channel

from dotaservice.protos.DotaService_grpc import DotaServiceStub
from dotaservice.protos.DotaService_pb2 import Actions, HeroPick, Team, Hero, HeroControlMode, ObserveConfig, HostMode
from dotaservice.protos.DotaService_pb2 import GameConfig
from dotaservice.protos.dota_gcmessages_common_bot_script_pb2 import CMsgBotWorldState


async def main():
    action = Actions(
        actions=CMsgBotWorldState.Actions(
            actions=[
                CMsgBotWorldState.Action(
                    actionType = CMsgBotWorldState.Action.Type.DOTA_UNIT_ORDER_MOVE_TO_POSITION,
                    moveToLocation = CMsgBotWorldState.Action.MoveToLocation(
                        location=CMsgBotWorldState.Vector(x=-394, y=-486, z=2)
                    )
                )
        ]),
        team_id=Team.TEAM_RADIANT
    )
    # Connect to the DotaService.
    env = DotaServiceStub(Channel('192.168.1.17', 13337))

    # Get the initial observation.
    observation = await env.reset(GameConfig(
        host_mode=HostMode.HOST_MODE_DEDICATED,
        hero_picks=[
            HeroPick(
                team_id=Team.TEAM_RADIANT, 
                hero_id=Hero.NPC_DOTA_HERO_PUDGE,
                control_mode=HeroControlMode.HERO_CONTROL_MODE_CONTROLLED
                ),
            HeroPick(
                team_id=Team.TEAM_RADIANT, 
                hero_id=Hero.NPC_DOTA_HERO_PUDGE,
                control_mode=HeroControlMode.HERO_CONTROL_MODE_DEFAULT
                ),
            HeroPick(
                team_id=Team.TEAM_RADIANT, 
                hero_id=Hero.NPC_DOTA_HERO_PUDGE,
                control_mode=HeroControlMode.HERO_CONTROL_MODE_DEFAULT
                ),
            HeroPick(
                team_id=Team.TEAM_RADIANT, 
                hero_id=Hero.NPC_DOTA_HERO_PUDGE,
                control_mode=HeroControlMode.HERO_CONTROL_MODE_DEFAULT
                ),
            HeroPick(
                team_id=Team.TEAM_RADIANT, 
                hero_id=Hero.NPC_DOTA_HERO_PUDGE,
                control_mode=HeroControlMode.HERO_CONTROL_MODE_DEFAULT
                ),
            HeroPick(
                team_id=Team.TEAM_DIRE, 
                hero_id=Hero.NPC_DOTA_HERO_PUDGE,
                control_mode=HeroControlMode.HERO_CONTROL_MODE_DEFAULT
                ),
            HeroPick(
                team_id=Team.TEAM_DIRE, 
                hero_id=Hero.NPC_DOTA_HERO_PUDGE,
                control_mode=HeroControlMode.HERO_CONTROL_MODE_DEFAULT
                ),
            HeroPick(
                team_id=Team.TEAM_DIRE, 
                hero_id=Hero.NPC_DOTA_HERO_PUDGE,
                control_mode=HeroControlMode.HERO_CONTROL_MODE_DEFAULT
                ),
            HeroPick(
                team_id=Team.TEAM_DIRE, 
                hero_id=Hero.NPC_DOTA_HERO_PUDGE,
                control_mode=HeroControlMode.HERO_CONTROL_MODE_DEFAULT
                ),
            HeroPick(
                team_id=Team.TEAM_DIRE, 
                hero_id=Hero.NPC_DOTA_HERO_PUDGE,
                control_mode=HeroControlMode.HERO_CONTROL_MODE_DEFAULT
                ),
        ],
        ticks_per_observation=30
        ))

    print(f"moving {action}")

    await env.act(action)
    while True:
        # Sample an action from the action protobuf
        # Take an action, returning the resulting observation.

        observation = await env.observe(ObserveConfig(team_id=Team.TEAM_RADIANT))
        print(observation)

if __name__ == '__main__':
    asyncio.run(main())
