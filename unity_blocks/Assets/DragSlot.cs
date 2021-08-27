using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DragSlot : MonoBehaviour
{
/// <summary>
/// Item slot class.
/// Store reference to the object inside slot.
/// </summary>
    // Reference to the item inside slot.
    public DragText currentItem;
    // Tells if slot is filled by other item.
    public bool SlotFilled => currentItem;
}
