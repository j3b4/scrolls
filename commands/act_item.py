from commands.command import Command
from world.utils.act import Announce, act
from world.utils.utils import is_cursed, is_equippable, is_obj, can_pickup, is_weapon, is_wieldable, is_wielded, is_worn


class CmdGet(Command):
    """
    get an object from room or a valid container

    Usage:
      get|take <obj>
      get|take 2.obj
      get|take <obj> from <container>
      get|take all.<obj> from all.<container>
    

    """

    key = "get"
    aliases = ['take']
    locks = "cmd:all()"
    arg_regex = r"\s|$"

    def func(self):
        """implements the command."""

        ch = self.caller
        if not self.args:
            ch.msg("Get what?")
            return

        args = self.args.strip().split()

        # example of get
        # get all
        # get book
        # get all.book
        # get 1.book from 1.bag
        # get all.book from all.bag
        # get all from 1.corpse
        # TODO: refactor this function
        if len(args) == 1:  #ex: get all.book, get 1.book, get book
            # attempt to find one item
            obj_name = args[0]
            if "." in obj_name:
                amt, obj_name = obj_name.split('.')
                if amt == 'all':
                    matched_objs = []
                    for obj in ch.location.contents:
                        if is_obj(obj):
                            if obj_name in obj.db.name:
                                matched_objs.append(obj)
                    if not matched_objs:
                        ch.msg(f"You couldn't find anything like {obj_name}")
                        return
                    for obj in matched_objs:
                        if can_pickup(ch, obj):
                            obj.move_to(ch)
                            act(f"$n picks up a $p.", True, True, ch, obj,
                                None, Announce.ToRoom)
                            act(f"You pick up a $p", False, False, ch, obj,
                                None, Announce.ToChar)
                        else:
                            act("You can't pick up $p", False, False, ch, None,
                                None, Announce.ToChar)
                    return
                else:
                    try:
                        amt = int(amt)
                    except ValueError:
                        ch.msg("specify integer when using order")
                        return
                    cntr = 0
                    for obj in ch.location.contents:
                        if is_obj(obj):
                            if obj_name in obj.db.name:
                                cntr += 1
                                if amt == cntr:
                                    if can_pickup(ch, obj):
                                        #this is the one
                                        obj.move_to(ch)
                                        act(f"$n picks up $p.", True, True, ch,
                                            obj, None, Announce.ToRoom)
                                        act(f"You pick up $p", False, False,
                                            ch, obj, None, Announce.ToChar)
                                        return
                                    else:
                                        act("You can't pick up $p", False,
                                            False, ch, None, None,
                                            Announce.ToChar)
                                        return
                    if cntr < amt:
                        ch.msg("There aren't that many around")
                        return
                    if cntr == amt:
                        ch.msg(
                            "obj should have returned before getting to this.. contact admin"
                        )
                        return
                    if amt < 0:
                        ch.msg("indexing with negatives? I don't think so..")
                        return
                    if cntr > amt:
                        ch.msg("this seriously would even make sense...")
                        return
            elif obj_name == 'all':
                for obj in ch.location.contents:
                    if is_obj(obj):
                        if can_pickup(ch, obj):
                            obj.move_to(ch, quiet=True)
                            act(f"$n picks up a $p.", True, True, ch, obj,
                                None, Announce.ToRoom)
                            act(f"You pick up a $p", False, False, ch, obj,
                                None, Announce.ToChar)
                        else:
                            act("You can't pick up $p", False, False, ch, None,
                                None, Announce.ToChar)
            else:
                # do a find in room, return first match
                for obj in ch.location.contents:
                    if is_obj(obj):
                        if obj_name in obj.db.name:
                            if can_pickup(ch, obj):
                                # move obj to player inv
                                obj.move_to(ch)
                                act(f"$n picks up a $p.", True, True, ch, obj,
                                    None, Announce.ToRoom)
                                act(f"You pick up a $p", False, False, ch, obj,
                                    None, Announce.ToChar)
                                return
                            else:
                                act("You can't pick up $p", False, False, ch,
                                    None, None, Announce.ToChar)


class CmdRemove(Command):
    """
    Remove a weapon or armor from your equipped equipment

    Usage:
        remove <obj>
        remove all
    """

    key = 'remove'
    locks = 'cmd:all()'

    def func(self):
        ch = self.caller
        if not self.args:
            ch.msg("What do you want to remove?")
            return

        obj_name = self.args.strip()

        success_remove = False
        for obj in ch.contents:
            if is_equippable(obj) and is_worn(obj) and not is_cursed(obj):
                # equipment
                if obj_name == 'all':
                    ch.equipment.remove(obj)
                    success_remove = True
                elif obj_name in obj.db.name:
                    ch.equipment.remove(obj)
                    return

            elif is_wieldable(obj) and is_wielded(obj) and not is_cursed(obj):
                # weapon
                if obj_name == 'all':
                    ch.equipment.unwield(obj)
                    success_remove = True

                elif obj_name in obj.db.name:
                    ch.equipment.unwield(obj)
                    return

        if not success_remove:
            ch.msg("You can't remove that")


class CmdDrop(Command):
    """
    drop something
    Usage:
      drop <obj>
      drop <obj>.all #TODO
      drop all
    """

    key = "drop"
    locks = "cmd:all()"
    arg_regex = r"\s|$"

    def func(self):
        """Implement command"""

        ch = self.caller
        if not self.args:
            ch.msg("Drop what?")
            return

        # Because the DROP command by definition looks for items
        # in inventory, call the search function using location = caller
        args = self.args.strip().split(' ')
        if len(args) == 1:

            all_objs = False
            for obj in ch.contents:
                if is_worn(obj) or is_wielded(obj):
                    continue

                success_drop = False
                if args[0] == 'all':
                    obj.move_to(ch.location, quiet=True)
                    success_drop = all_objs = True
                elif args[0] in obj.db.name:
                    obj.move_to(ch.location, quiet=True)
                    success_drop = True

                if success_drop:
                    act("$n drops $p", True, True, ch, obj, None,
                        Announce.ToRoom)
                    act("You drop $p", True, True, ch, obj, None,
                        Announce.ToChar)
                else:
                    ch.msg("You can't drop that")
                if not all_objs:
                    return


class CmdWield(Command):
    """
    wield a weapon

    Usage:
        wield <obj>
    """
    key = 'wield'
    locks = 'cmd:all()'

    def func(self):
        ch = self.caller

        if not self.args:
            ch.msg("What do you want to wield?")
            return

        args = self.args.strip()
        for obj in ch.contents:
            if is_weapon(obj) and not is_wielded(obj):
                # potential candidate
                if args in obj.db.name:
                    # match
                    ch.equipment.wield(obj)
                    return

        ch.msg("You couldn't find anything like that to wield.")


class CmdWear(Command):
    """
    Dawn a piece of armor onto you from
    your inventory

    Usage:
        wear <obj>
        wear all
    """

    key = 'wear'
    locks = 'cmd:all()'

    def func(self):
        ch = self.caller

        if not self.args:
            ch.msg("What do you want to wear?")
            return

        args = self.args.strip()
        if args == 'all':
            for obj in ch.contents:
                if is_equippable(
                        obj) and not is_worn(obj) and not is_weapon(obj):
                    ch.equipment.add(obj)
            return
        for obj in ch.contents:
            if is_equippable(obj) and not is_worn(obj) and not is_weapon(obj):
                # this object is a potential candidate
                if args in obj.db.name:
                    # we have a match!
                    ch.equipment.add(obj)
                    return
        ch.msg("You couldn't find anything like that to wear")